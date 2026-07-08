---
id: UNC@20.15.2@MMLCommand@LST PGWBACKOFF
type: MMLCommand
name: LST PGWBACKOFF（查询P-GW Back-off流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PGWBACKOFF
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- P-GW Backoff流控管理
status: active
---

# LST PGWBACKOFF（查询P-GW Back-off流控参数）

## 功能

**适用网元：MME**

该命令用于查询P-GW Back-off流控参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PGWBACKOFF]] · P-GW Back-off流控参数（PGWBACKOFF）

## 使用实例

查询P-GW Back-off流控参数：

LST PGWBACKOFF:;

```
%%LST PGWBACKOFF:;%%

操作结果如下
--------------
 流控开关  =  开
APNNI组号  =  2
 P-GW组号  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PGWBACKOFF.md`
