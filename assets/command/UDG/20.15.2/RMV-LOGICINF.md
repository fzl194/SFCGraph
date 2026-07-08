---
id: UDG@20.15.2@MMLCommand@RMV LOGICINF
type: MMLCommand
name: RMV LOGICINF（删除逻辑接口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: LOGICINF
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- DN管理
- 逻辑接口管理
- 逻辑接口配置
- 接口
status: active
---

# RMV LOGICINF（删除逻辑接口）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](删除逻辑接口（RMV LOGICINF）_82835380.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此操作会删除逻辑接口，可能导致相关业务中断。

该命令用于删除指定的逻辑接口。

## 注意事项

- 该命令执行后立即生效。
- 删除的逻辑接口需为系统中存在的逻辑接口，否则命令执行失败。
- 若逻辑接口被IPFarm等对象绑定时，则不允许被删除。
- 若giif逻辑口被L2TP组或APN绑定时，逻辑口不允许被删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 逻辑接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置逻辑接口名称，确保逻辑接口的唯一性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 字符串形式，用户输入形式例如：n4if1/0/0。其中n4if为逻辑接口类型；1/0/0中第一个数字为ISU组号，第二个数字为实例类型；第三个数字为逻辑接口号，各逻辑接口类型有各自的配置范围。<br>- 逻辑接口类型：giif，s5-sif，s1-uif，saif，paif，grpif，phif，s11-uif，nxccif，nxucif，n4if，n3if，n9cif，scif，vxlanif，n19if，tm3if，tx-uif，n6mbif，n3mbif，sgimbif，m1if，gcfif，swuif，swmif。（其中nxccif为预置接口，配置后只允许执行ping操作。）。<br>- ISU组号：1。<br>- ISU实例类型：0~64。0表示组级类型，1~64表示Instance级类型。<br>- ISU实例类型为0时，逻辑接口号：giif：0~1023，grpif：0，phif：0~2047，nxccif：0，n4if：0，tm3if：0，gcfif：0，swuif：0，swmif：0~15。<br>- ISU实例类型为1时，逻辑接口号：s5-sif：0~31，s1-uif：0~31，saif：0~31，paif：0~31，s11-uif：0~31，nxucif：0~31，n3if：0~31，n9cif：0~31，scif：0~31，vxlanif：0~31，n19if：0~31，tx-uif：0，n6mbif：0，n3mbif：0~31。<br>- ISU实例类型为2~64时，逻辑接口号: s5-sif：0，s1-uif：0，saif：0，paif：0，n3if：0，n9cif：0，scif：0。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LOGICINF]] · 逻辑接口（LOGICINF）

## 使用实例

删除逻辑接口n4if1/0/0：

```
RMV LOGICINF: NAME="n4if1/0/0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-LOGICINF.md`
