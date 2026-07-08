---
id: UNC@20.15.2@MMLCommand@LST MSISDNSUBGPMEM
type: MMLCommand
name: LST MSISDNSUBGPMEM（查询MSISDN用户群成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MSISDNSUBGPMEM
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- MSISDN用户群成员管理
status: active
---

# LST MSISDNSUBGPMEM（查询MSISDN用户群成员）

## 功能

**适用网元：SGSN、MME**

此命令用于查询MSISDN用户群成员记录。

## 注意事项

此命令用于查询MSISDN用户群成员记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：可选参数<br>参数含义：待查询的用户群标识。<br>数据来源：整网规划<br>取值范围：1～100。<br>默认值：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：可选参数<br>参数含义：待查询的用户群成员的MSISDN前缀。<br>取值范围：1～15位十进制数字。<br>默认值：无<br>说明：支持最大匹配的查询方式。 |

## 操作的配置对象

- [MSISDN用户群成员（MSISDNSUBGPMEM）](configobject/UNC/20.15.2/MSISDNSUBGPMEM.md)

## 使用实例

查询一条用户群标识为30的MSISDN用户群成员记录：

LST MSISDNSUBGPMEM: SUBID=30;

```
%%LST MSISDNSUBGPMEM: SUBID=30;%%
RETCODE = 0  操作成功

操作结果如下
--------------
 用户群标识  =  30
MSISDN前缀  =  12345
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MSISDN用户群成员(LST-MSISDNSUBGPMEM)_72225251.md`
