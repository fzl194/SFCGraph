---
id: UDG@20.15.2@MMLCommand@ADD L2TPCLIENTIP
type: MMLCommand
name: ADD L2TPCLIENTIP（增加L2TP绑定的接口）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: L2TPCLIENTIP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1500
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP组绑定源端接口
status: active
---

# ADD L2TPCLIENTIP（增加L2TP绑定的接口）

## 功能

**适用NF：PGW-U、UPF**

该命令用于在L2TP组上绑定指定的源端Gi接口。L2TP用户入网场景，系统可以使用此接口作为源端接口与LNS进行交互。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1500。
- 每个L2TP组只能绑定1个源端接口。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2TPGROUPID | L2TP组号 | 可选必选说明：必选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：该参数使用ADD L2TPGROUP命令配置生成。 |
| INTERFACENAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：指定源端Gi接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD LOGICINF命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPCLIENTIP]] · L2TP绑定的接口（L2TPCLIENTIP）

## 关联任务

- [[UDG@20.15.2@Task@0-00135]]

## 使用实例

假设L2TP用户要入网，要使用"giif1/0/0"接口作为L2TP组1与LNS交互时的源端接口，可以使用该命令配置：

```
ADD L2TPCLIENTIP:L2TPGROUPID=1,INTERFACENAME="giif1/0/0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-L2TPCLIENTIP.md`
