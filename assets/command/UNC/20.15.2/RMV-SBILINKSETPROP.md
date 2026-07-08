---
id: UNC@20.15.2@MMLCommand@RMV SBILINKSETPROP
type: MMLCommand
name: RMV SBILINKSETPROP（删除SBI链路集策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SBILINKSETPROP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路集策略管理
status: active
---

# RMV SBILINKSETPROP（删除SBI链路集策略）

## 功能

![](删除SBI链路集策略（RMV SBILINKSETPROP）_29291777.assets/notice_3.0-zh-cn_2.png)

该命令用于删除SBI链路集策略，该策略删除以后，使用该策略的链路集的LINKNUMPERPROC会变化为默认值1，可能导致单链路上负载过大，一旦网络传输质量变化，容易出现该链路上的传输拥塞导致丢包，可能影响业务。

该命令用于删除SBI链路集策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SBI链路集策略的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SBI链路集策略（SBILINKSETPROP）](configobject/UNC/20.15.2/SBILINKSETPROP.md)

## 使用实例

若运营商想删除索引为1的SBI链路集策略，可以执行如下命令：

```
RMV SBILINKSETPROP: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SBI链路集策略（RMV-SBILINKSETPROP）_29291777.md`
