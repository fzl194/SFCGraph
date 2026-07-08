---
id: UNC@20.15.2@MMLCommand@LST PORTGROUP
type: MMLCommand
name: LST PORTGROUP（查询端口组配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PORTGROUP
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

# LST PORTGROUP（查询端口组配置）

## 功能

该命令用于显示端口组配置信息。

当不指定PORTGROUPNAME参数时，查询设备上所有端口组的信息；当指定PORTGROUPNAME参数时，可以查询指定端口组的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PORTGROUPNAME | 端口组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示端口组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PORTGROUP]] · 端口组（PORTGROUP）

## 使用实例

查询端口组ifm的配置信息：

```
LST PORTGROUP:;
```

```
        RETCODE = 0  操作成功

        结果如下
        ------------------------
        端口组名称 = ifm
    (结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询端口组配置（LST-PORTGROUP）_49962022.md`
