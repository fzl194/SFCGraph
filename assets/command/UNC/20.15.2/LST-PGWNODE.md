---
id: UNC@20.15.2@MMLCommand@LST PGWNODE
type: MMLCommand
name: LST PGWNODE（查询P-GW局向）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PGWNODE
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
- 业务安全管理
- 会话管理
- P-GW信息管理
- P-GW节点管理
status: active
---

# LST PGWNODE（查询P-GW局向）

## 功能

**适用网元：SGSN、MME**

该命令用于查询P-GW局向。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | P-GW组号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定P-GW组号。<br>数据来源：本端规划<br>取值范围：0～15<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PGWNODE]] · P-GW局向（PGWNODE）

## 使用实例

查询P-GW组号为2的局向信息：

LST PGWNODE: GRPID=2;

```
%%LST PGWNODE: GRPID=2;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
         P-GW组号  =  2
P-GW Nodename后缀  =  GW01.CITY-B.PROVINCE-A.NODE.EPC.MNC000.MCC460.3GPPNETWORK.ORG
             描述  =  noname
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PGWNODE.md`
