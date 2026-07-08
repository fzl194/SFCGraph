---
id: UDG@20.15.2@MMLCommand@RMV TIMERANGE
type: MMLCommand
name: RMV TIMERANGE（删除时间段）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TIMERANGE
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 时间规则管理
- 时间段
status: active
---

# RMV TIMERANGE（删除时间段）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除一个时间段配置。当系统的业务不再需要在特定的时间段内生效时，使用此命令进行删除时间段配置。

## 注意事项

- 该命令执行后立即生效。
- 如果时间段已经被绑定到Rule、ContCateGBind、AclBindApn或者BwmRule则不允许删除，需先解除绑定，才能删除。
- 如果时间段下已经配置了周期时间段和绝对时间段，删除时间段配置时也一并删除重名的周期时间段和绝对时间段对应的记录。配置回退的时候需要增加周期和绝对时间段。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMERANGENAME | 时间段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置时间段的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写，以字母开头。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TIMERANGE]] · 时间段（TIMERANGE）

## 使用实例

- 假设运营商需要删除一个时间段，名字为t1，则按如下命令配置：
  ```
  RMV TIMERANGE:TIMERANGENAME="t1";
  ```
- 假设运营商需要删除配置的所有时间段，则按如下命令配置：
  ```
  RMV TIMERANGE:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-TIMERANGE.md`
