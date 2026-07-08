---
id: UDG@20.15.2@MMLCommand@RMV SBILINKCFG
type: MMLCommand
name: RMV SBILINKCFG（删除SBI接口链路属性配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SBILINKCFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路属性管理
status: active
---

# RMV SBILINKCFG（删除SBI接口链路属性配置）

## 功能

![](删除SBI接口链路属性配置（RMV SBILINKCFG）_29213291.assets/notice_3.0-zh-cn.png)

如果删除配置，可能导致链路数量变化，触发拆链或者新建链路。链路数变多可能会超过对端链路规格限制，导致建链失败；链路数变少可能会导致单链路负载增高，存在单链路过载风险，而且可能会导致对端负载不均衡。

该命令用于删除服务化接口的静态链路，也可以用于删除服务化接口动态链路的属性配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果删除了静态链路，则该链路上承载的业务中断。
> - 如果删除了动态链路的属性配置，如果系统开启了链路自动控制功能，则系统按自动控制功能控制链路数量；如果系统未开启俩路自动控制功能，则系统按默认设置控制链路梳理。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务化接口链路的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~513。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SBI接口链路属性配置（SBILINKCFG）](configobject/UDG/20.15.2/SBILINKCFG.md)

## 使用实例

- 若运营商想删除索引为1的服务化接口静态链路，可以执行如下命令：
  ```
  RMV SBILINKCFG: INDEX=1;
  ```
- 若运营商想删除索引为2的服务化接口动态链路的属性配置，可以执行如下命令：
  ```
  RMV SBILINKCFG: INDEX=2;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除SBI接口链路属性配置（RMV-SBILINKCFG）_29213291.md`
