---
id: UNC@20.15.2@MMLCommand@LST SUBGP
type: MMLCommand
name: LST SUBGP（查询用户群）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SUBGP
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- 用户群管理
status: active
---

# LST SUBGP（查询用户群）

## 功能

**适用网元：SGSN、MME**

该命令用于查询用户群的记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：可选参数<br>参数含义：待查询的用户群标识。<br>取值范围：1～100<br>默认值：无 |

## 操作的配置对象

- [用户群（SUBGP）](configobject/UNC/20.15.2/SUBGP.md)

## 使用实例

查询一条用户群标识为1的用户群管理记录：

LST SUBGP: SUBID=1;

```
%%LST SUBGP: SUBID=1;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
用户群标识  =  1
用户群名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户群(LST-SUBGP)_26145562.md`
