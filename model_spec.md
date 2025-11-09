# Математико-экономическая модель оптимального планирования разработки игр в студии SeptetGaming

## Постановка задачи

Студия **SeptetGaming** выпускает проекты различных типов
$i \in \mathcal{I}$ (жанры и подтипы игр) в течение горизонта
планирования $T = 120$ месяцев. Каждый проект требует ресурсы трёх
отделов $d \in \mathcal{D} = \{GP, GR, S\}$: геймплей, графика и
анимации, звук. Проекты приносят прибыль $Profit_i$ и имеют длительность
$Dur_i$.

Необходимо определить, *в каком месяце запускать проекты каждого типа*,
чтобы максимизировать совокупную прибыль при ограничениях по ресурсам и
обязательствам перед издателем.

---
## Переменные

$$\begin{array}{ll}
T = 120 & \text{горизонт планирования (120 месяцев)}\\
i \in \mathcal{[AAA, AA, DLC ... SimNoMobile, SimVR]} & \text{тип проекта}\\
t \in \mathcal{[1 ... T]} & \text{месяц старта проекта}\\
d \in \mathcal{[gameplay, graphics, sound]} & \text{отдел}\\
g \in \mathcal{[rpg, simulator, strategy]} \\
Profit_i & \text{прибыль от проекта типа $i$ (тыс. усл. ед.)}\\
H_{i,d} & \text{трудоёмкость проекта $i$ в отделе $d$ (часы)}\\
Dur_i & \text{длительность проекта $i$ (мес.)}\\
Cap_{d,m} & \text{мощность отдела $d$ в месяце $m$ (часы)}\\
MaxConcurrent_d & \text{макс. число активных проектов отдела $d$}\\
MinReq_i, MinReq_g & \text{минимальное количество проектов по типам и жанрам}
\end{array}$$

$$x_{i,t} =
\begin{cases}
1, & \text{если проект типа $i$ стартует в месяце $t$;}\\
0, & \text{иначе.}
\end{cases}$$

## Целевая функция

$$\max Z = \sum_{i \in \mathcal{I}} \sum_{t=1}^{T} Profit_i \cdot x_{i,t}$$

`Цель - максимизировать суммарную прибыль всех проектов за 10 лет.`
## Ограничения

### 1. Ограничения по ресурсам отделов (ежемесячные мощности)

Для каждого месяца $m$ и отдела $d$ суммарные часы всех активных
проектов не должны превышать доступную мощность:

$$\sum_{i \in \mathcal{I}} \sum_{t=1}^{T}
x_{i,t} \cdot Active_{i,t,m} \cdot
\frac{H_{i,d}}{Dur_i}
\;\le\;
Cap_{d,m},
\quad
\forall d \in \mathcal{D},\; m = 1,\ldots,T$$

где $Active_{i,t,m}=1$, если проект $i$, начатый в месяце $t$, активен в
месяце $m$: $$Active_{i,t,m} =
\begin{cases}
1, & \text{если } t \le m < t + Dur_i,\\
0, & \text{иначе.}
\end{cases}$$

### 2. Ограничения на количество одновременно активных проектов

Ограничение по управляемости --- в каждый момент времени отдел не может
работать более чем с $MaxConcurrent_d$ активными проектами:

$$\sum_{i \in \mathcal{I}} \sum_{t=1}^{T} x_{i,t} \cdot Active_{i,t,m}
\;\le\;
MaxConcurrent_d,
\quad \forall d \in \mathcal{D},\; m = 1,\ldots,T$$

### 3. Ограничение на запуск проектов в месяц

Не более одного старта проекта каждого типа в месяц:

$$x_{i,t} \le 1, \quad \forall i,t$$

### 4. Минимальные обязательства издателя

$$\sum_{t=1}^{T} x_{i,t} \ge MinReq_i, \quad \forall i \in \mathcal{I}$$

$$\sum_{i \in g} \sum_{t=1}^{T} x_{i,t} \ge MinReq_g, \quad \forall g \in \mathcal{G}$$

### 5. Целочисленность переменных

$$x_{i,t} \in \{0,1\}, \quad \forall i,t$$

---

## Общая модель

### Переменные

$$\begin{cases}
T = 120 & \text{горизонт планирования (120 месяцев)}\\
i \in \mathcal{[AAA, AA, DLC ... SimNoMobile, SimVR]} & \text{тип проекта}\\
t \in \mathcal{[1 ... T]} & \text{месяц старта проекта}\\
d \in \mathcal{[gameplay, graphics, sound]} & \text{отдел}\\
g \in \mathcal{[rpg, simulator, strategy]} \\
Profit_i & \text{прибыль от проекта типа $i$ (тыс. усл. ед.)}\\
H_{i,d} & \text{трудоёмкость проекта $i$ в отделе $d$ (часы)}\\
Dur_i & \text{длительность проекта $i$ (мес.)}\\
Cap_{d,m} & \text{мощность отдела $d$ в месяце $m$ (часы)}\\
MaxConcurrent_d & \text{макс. число активных проектов отдела $d$}\\
MinReq_i, MinReq_g & \text{минимальное количество проектов по типам и жанрам}
\end{cases}$$

### Целевая функция
$$\begin{cases}
\max Z = \sum_{i \in \mathcal{I}} \sum_{t=1}^{T} Profit_i \cdot x_{i,t}\\
x_{i,t} =
\begin{cases}
1, & \text{если проект типа $i$ стартует в месяце $t$;}\\
0, & \text{иначе.}
\end{cases}
\end{cases}$$

### Ограничения

$$
\begin{cases}
x_{i,t} \in \{0,1\}, \quad \forall i,t\\
x_{i,t} \le 1, \quad \forall i,t\\
Active_{i,t,m} = t \le m < t + Dur_i, \quad Active_{i,t,m} \in \{0,1\} \\
\sum_{i \in \mathcal{I}} \sum_{t=1}^{T} x_{i,t} \cdot Active_{i,t,m} \cdot \frac{H_{i,d}}{Dur_i} \;\le\; Cap_{d,m}, \quad \forall d \in \mathcal{D},\; m = 1,\ldots,T\\
\sum_{i \in \mathcal{I}} \sum_{t=1}^{T} x_{i,t} \cdot Active_{i,t,m}
\;\le\;
MaxConcurrent_d,
\quad \forall d \in \mathcal{D},\; m = 1,\ldots,T\\
\sum_{t=1}^{T} x_{i,t} \ge MinReq_i, \quad \forall i \in \mathcal{I}\\
\sum_{i \in g} \sum_{t=1}^{T} x_{i,t} \ge MinReq_g, \quad \forall g \in \mathcal{G}\\
\end{cases}$$
