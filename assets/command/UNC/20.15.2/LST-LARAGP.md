---
id: UNC@20.15.2@MMLCommand@LST LARAGP
type: MMLCommand
name: LST LARAGP（查询位置区群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LARAGP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 位置区管理
- 位置区群组管理
status: active
---

# LST LARAGP（查询位置区群组）

## 功能

**适用网元：SGSN**

此命令用于查询位置区和路由区的区域群。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LARAGPID | 区域群标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区和路由区的区域群标识。<br>数据来源：整网规划<br>取值范围：1～2048<br>默认值：无 |

## 操作的配置对象

- [位置区群组（LARAGP）](configobject/UNC/20.15.2/LARAGP.md)

## 使用实例

查询所有位置区群组记录：

LST LARAGP:;

```
%%LST LARAGP:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
区域群标识  =  55
区域群名称  =  shanghai
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询位置区群组(LST-LARAGP)_72225163.md`
