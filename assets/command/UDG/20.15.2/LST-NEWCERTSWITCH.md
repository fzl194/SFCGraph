---
id: UDG@20.15.2@MMLCommand@LST NEWCERTSWITCH
type: MMLCommand
name: LST NEWCERTSWITCH（查询证书开关状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NEWCERTSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 证书维护
status: active
---

# LST NEWCERTSWITCH（查询证书开关状态）

## 功能

查询证书开关状态。

> **说明**
> - [**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)命令触发开关切换，请1~3分钟后使用[**LST NEWCERTSWITCH**](查询证书开关状态（LST NEWCERTSWITCH）_59336676.md)命令查询开关切换任务结果。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/NEWCERTSWITCH]] · 证书开关状态（NEWCERTSWITCH）

## 使用实例

查询证书开关状态。

```
%%LST NEWCERTSWITCH:;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
    证书开关  =  开 
    加载状态  =  成功 
(结果个数 = 1)  

---    END
```

证书开关状态切换失败时，查询证书开关状态。

```
%%LST NEWCERTSWITCH:;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
    证书开关  =  开 
    加载状态  =  失败 
(结果个数 = 1)  

失败服务信息如下
------------ 
网元ID   失败服务名称   节点信息
0        Privilege      172.16.1.1
(结果个数 = 1) 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询证书开关状态（LST-NEWCERTSWITCH）_59336676.md`
