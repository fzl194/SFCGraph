---
id: UNC@20.15.2@MMLCommand@LST SMCOMMTIMER
type: MMLCommand
name: LST SMCOMMTIMER（查询通用会话管理定时器参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMCOMMTIMER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话协议定时器管理
- 通用会话协议定时器
status: active
---

# LST SMCOMMTIMER（查询通用会话管理定时器参数）

## 功能

**适用NF：PGW-C、SMF、GGSN、SGW-C**

该命令用于查询2、3、4、5G会话管理通用的定时器时长及重发间隔等参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMCOMMTIMER]] · 通用会话管理定时器参数（SMCOMMTIMER）

## 使用实例

查询通用会话管理定时器参数：

```
%%LST SMCOMMTIMER:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                          等待策略响应定时器时长(s)  =  60
                          等待计费响应定时器时长(s)  =  10
                      等待PFCP实体响应定时器时长(s)  =  3
                        等待Radius响应定时器时长(s)  =  30
                      等待GTPC实体响应定时器时长(s)  =  10
                                  间接转发定时器(s)  =  3
                                  寻呼定时器时长(s)  =  10
                    等待DNS Server响应定时器时长(s)  =  20
                 SR相关流程释放老侧U面资源定时器(s)  =  10
                 Xn切换流程释放老侧U面资源定时器(s)  =  10
                判断GTPC请求消息为重发消息的时长(s)  =  10
          插入I-SMF流程发起PDU会话重建定时器时长(ms) = 0
        故障后数据恢复期间消息缓存老化定时器时长(s)  =  5
         N2切换流程释放老侧I-SMF/V-SMF资源定时器(s)  =  10
		              快速去活流程定时器(s)  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMCOMMTIMER.md`
