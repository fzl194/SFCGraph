---
id: UDG@20.15.2@MMLCommand@LST PORTGROUPMEMBER
type: MMLCommand
name: LST PORTGROUPMEMBER（查询端口组成员配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PORTGROUPMEMBER
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 端口组
status: active
---

# LST PORTGROUPMEMBER（查询端口组成员配置）

## 功能

该命令用于显示端口组成员信息。

当不指定PORTGROUPNAME参数时，查询设备上所有端口组的成员信息；当指定PORTGROUPNAME参数时，可以查询指定端口组的成员配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PORTGROUPNAME | 端口组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示端口组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |

## 操作的配置对象

- [端口组成员（PORTGROUPMEMBER）](configobject/UDG/20.15.2/PORTGROUPMEMBER.md)

## 使用实例

查询端口组ifm的成员信息：

```
LST PORTGROUPMEMBER:PORTGROUPNAME="ifm";
```

```
    RETCODE = 0  操作成功

    结果如下
    ------------------------
    成员接口名     端口组
    LoopBack1      ifm
    LoopBack2      ifm
    LoopBack3      ifm
    LoopBack4      ifm
    (结果个数 = 4)
---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询端口组成员配置（LST-PORTGROUPMEMBER）_49961894.md`
