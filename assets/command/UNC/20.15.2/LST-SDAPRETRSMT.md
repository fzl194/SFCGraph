---
id: UNC@20.15.2@MMLCommand@LST SDAPRETRSMT
type: MMLCommand
name: LST SDAPRETRSMT（查询Sdup接口可靠性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SDAPRETRSMT
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- Sdup接口管理
- Sdup消息重传参数管理
status: active
---

# LST SDAPRETRSMT（查询Sdup接口可靠性）

## 功能

**适用网元：MME**

本命令用于查询Sdup接口的消息传输可靠性管理的参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [Sdup接口可靠性（SDAPRETRSMT）](configobject/UNC/20.15.2/SDAPRETRSMT.md)

## 使用实例

查询Sdup接口的消息传输可靠性管理的参数：

LST SDAPRETRSMT:;

```
%%LST SDAPRETRSMT:;%%
RETCODE = 0  操作成功

操作结果如下：
-------------------------
 Sdup接口消息分类  T-RESPONSE  N-REQUEST

 链路管理消息      5           4        
 备份管理消息      5           4        
 恢复管理消息      1           1        
 其他消息          5           4
(结果个数 = 4)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Sdup接口可靠性(LST-SDAPRETRSMT)_26147294.md`
