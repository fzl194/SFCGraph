---
id: UDG@20.15.2@MMLCommand@SET DRAUTOSWOVER
type: MMLCommand
name: SET DRAUTOSWOVER（设置在热备容灾模式下是否开启自动倒换功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DRAUTOSWOVER
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET DRAUTOSWOVER（设置在热备容灾模式下是否开启自动倒换功能）

## 功能

该命令用于设置在热备容灾模式下是否开启自动倒换功能。

> **说明**
> - 该命令执行后立即生效。
>
> - 为避免频繁执行对系统性能产生冲击，该命令在三分钟之内只能执行一次。
> - 如果系统时间发生跳变，跳变到上一次执行本命令的前N（N<=3）分钟，下一次可执行本命令最少需等待N+3分钟。
> - 以521软参的优先级最高，当521软参设置为1时，即便满足自动倒回条件也不会触发。当设置为0时，则以本命令设置为准。
> - 开关开时，该功能受备升主次数限制，即达到次数，由自动倒回触发的倒换无法成功。
> - 该命令仅在配置备容灾实例生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | AUTOSWOVER | WAITTIME |
> | --- | --- |
> | DISABLE | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AUTOSWOVER | 自动倒回功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制在热备容灾模式下是否开启自动倒回功能。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（开启）”：开启自动倒回功能。<br>- “DISABLE（关闭）”：关闭自动倒回功能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DRAUTOSWOVER查询当前参数配置值。<br>配置原则：无 |
| WAITTIME | 等待时间(分钟) | 可选必选说明：该参数在"AUTOSWOVER"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置满足自动倒回条件后的等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~60。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DRAUTOSWOVER查询当前参数配置值。<br>配置原则：<br>开启自动倒回时建议配置为5。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DRAUTOSWOVER]] · 热备模式下是否开启自动倒换功能（DRAUTOSWOVER）

## 使用实例

- 开启热备容灾模式下自动倒换功能
  ```
  SET DRAUTOSWOVER: AUTOSWOVER=ENABLE;
  ```
- 关闭热备容灾模式下自动倒换功能
  ```
  SET DRAUTOSWOVER: AUTOSWOVER=DISABLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置在热备容灾模式下是否开启自动倒换功能（SET-DRAUTOSWOVER）_28275349.md`
