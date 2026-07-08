---
id: UDG@20.15.2@MMLCommand@ADD L2TPRDSCLIENT
type: MMLCommand
name: ADD L2TPRDSCLIENT（增加APN绑定的L2TP接口）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: L2TPRDSCLIENT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- APN绑定L2TP接口
status: active
---

# ADD L2TPRDSCLIENT（增加APN绑定的L2TP接口）

## 功能

**适用NF：PGW-U、UPF**

该命令用于在APN上指定的源端Gi接口绑定关系。在AAA返回L2TP属性启动L2TP业务场景，该接口可用做系统与LNS进行交互时的源端接口。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条L2tpRdsClient。
- 每个APN可以绑定1个源端接口。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| INTERFACENAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：指定源端Gi接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD LOGICINF命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPRDSCLIENT]] · APN绑定的L2TP接口（L2TPRDSCLIENT）

## 关联任务

- [[UDG@20.15.2@Task@0-00134]]

## 使用实例

假设用户要为指定的APN “huawei.com”绑定源端接口"giif1/0/0"，需要先确保指定的APN实例已经存在：

```
ADD L2TPRDSCLIENT:APN="huawei.com",INTERFACENAME="giif1/0/0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-L2TPRDSCLIENT.md`
