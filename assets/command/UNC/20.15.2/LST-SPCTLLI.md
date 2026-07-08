---
id: UNC@20.15.2@MMLCommand@LST SPCTLLI
type: MMLCommand
name: LST SPCTLLI（查询特殊随机TLLI配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SPCTLLI
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
- 特殊TLLI配置
status: active
---

# LST SPCTLLI（查询特殊随机TLLI配置）

## 功能

**适用网元：SGSN**

该命令用于查询特殊RANDOM TLLI的配置记录。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TLLI | TLLI | 可选必选说明：可选参数<br>参数含义：该参数用于指定RANDOM TLLI。<br>数据来源：网上问题<br>取值范围： 0x00000000～0xffffffff(十六进制)<br>默认值：无 |

## 操作的配置对象

- [特殊随机TLLI配置（SPCTLLI）](configobject/UNC/20.15.2/SPCTLLI.md)

## 使用实例

查询特殊RANDOM TLLI的配置记录：

**LST SPCTLLI:;**

```
%%LST SPCTLLI:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
    TLLI  =  0x71234ABC
手机信息  =  none
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询特殊随机TLLI配置(LST-SPCTLLI)_26145496.md`
