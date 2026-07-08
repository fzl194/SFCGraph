---
id: UDG@20.15.2@MMLCommand@RMV UPREALMBINDAPN
type: MMLCommand
name: RMV UPREALMBINDAPN（删除APN与Diameter Realm关联关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPREALMBINDAPN
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- Diameter Realm
- Realm绑定APN
status: active
---

# RMV UPREALMBINDAPN（删除APN与Diameter Realm关联关系）

## 功能

**适用NF：UPF**

![](删除APN与Diameter Realm关联关系（RMV UPREALMBINDAPN）_97080165.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除APN与Diameter Realm的关联关系，可能会影响DRA的选择。

该命令用于删除APN对应的Diameter域信息，或撤销通过IMSI构造Diameter域信息的方式。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要与Diameter域绑定的APN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN绑定Diameter域的Diameter应用类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：根据实际应用场景选择对应的枚举值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPREALMBINDAPN]] · APN与Diameter Realm关联关系（UPREALMBINDAPN）

## 使用实例

由于业务变动，APN isp接入的用户不再支持SWM应用，则删除APN ISP下SWM应用绑定的Diameter域信息：

```
RMV UPREALMBINDAPN: APN="isp", APPLICATION=SWM;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-UPREALMBINDAPN.md`
