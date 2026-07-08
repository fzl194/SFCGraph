---
id: UDG@20.15.2@MMLCommand@RMV UPGLBDIAMREALM
type: MMLCommand
name: RMV UPGLBDIAMREALM（删除全局Diameter域）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPGLBDIAMREALM
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- Diameter Realm
- 全局Realm
status: active
---

# RMV UPGLBDIAMREALM（删除全局Diameter域）

## 功能

**适用NF：UPF**

![](删除全局Diameter域（RMV UPGLBDIAMREALM）_97080163.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除系统缺省的Diameter域，可能会影响DRA选择。

该命令用于删除全局Diameter域。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定全局Diameter域所属的Diameter应用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：根据实际应用场景选择对应的枚举值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPGLBDIAMREALM]] · 全局Diameter域（UPGLBDIAMREALM）

## 使用实例

如果SWM应用不再使用Diameter域，则使用命令删除SWM应用的Diameter域：

```
RMV UPGLBDIAMREALM: APPLICATION=SWM;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-UPGLBDIAMREALM.md`
