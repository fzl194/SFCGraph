---
id: UNC@20.15.2@MMLCommand@LST BGPCONFED
type: MMLCommand
name: LST BGPCONFED（查询联盟中自治系统）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BGPCONFED
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 联盟中自治系统
status: active
---

# LST BGPCONFED（查询联盟中自治系统）

## 功能

该命令用于查询联盟中子自治系统号。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONFEDASNUMBER | 联盟对等体的自治域号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定与本地AS连接的其他EBGP对等体所属的子自治系统号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～11。取值范围是number<1-4294967295>或者number<1-65535>.number<0-65535>。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BGPCONFED]] · 联盟中自治系统（BGPCONFED）

## 使用实例

查询联盟中子自治系统号：

```
LST BGPCONFED:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
联盟对等体的自治域号  =  65002
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询联盟中自治系统（LST-BGPCONFED）_00841113.md`
