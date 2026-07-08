---
id: UNC@20.15.2@MMLCommand@LST SMSCBLACKLIST
type: MMLCommand
name: LST SMSCBLACKLIST（查询SMSC黑名单记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSCBLACKLIST
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 短消息
- SMSC黑名单
status: active
---

# LST SMSCBLACKLIST（查询SMSC黑名单记录）

## 功能

**适用网元：SGSN**

该命令用于查询SMSC黑名单记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [SMSC黑名单记录（SMSCBLACKLIST）](configobject/UNC/20.15.2/SMSCBLACKLIST.md)

## 使用实例

查询SMSC黑名单记录：

LST SMSCBLACKLIST:;

```
%%LST SMSCBLACKLIST:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 SMSC地址  

 8613951701
 8613951998
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSC黑名单记录(LST-SMSCBLACKLIST)_72345323.md`
