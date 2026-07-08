---
id: UNC@20.15.2@MMLCommand@LST SMTIMER
type: MMLCommand
name: LST SMTIMER（查询5GC会话管理定时器参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMTIMER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话协议定时器管理
- 5GC会话协议定时器
status: active
---

# LST SMTIMER（查询5GC会话管理定时器参数）

## 功能

**适用NF：SMF**

该命令用于查询5GC会话管理定时器时长和消息重发次数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [5GC会话管理定时器参数（SMTIMER）](configobject/UNC/20.15.2/SMTIMER.md)

## 使用实例

查询5GC会话管理定时器时长和消息重发次数，执行如下命令：

```
%%LST SMTIMER:;%%
RETCODE = 0 操作成功

结果如下
------------------------
	  LADN超时释放时间(秒)  =  60
                     T3591(秒)  =  10
                     N3591(次)  =  3
                     T3593(秒)  =  30
                     T3592(秒)  =  10
                     N3592(次)  =  3
     等待UDM响应定时器时长(秒)  =  10
     等待AMF响应定时器时长(秒)  =  10
   等待I-SMF响应定时器时长(秒)  =  10
   等待H-SMF响应定时器时长(秒)  =  10
EPS Fallback保护定时器时长(秒)  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5GC会话管理定时器参数（LST-SMTIMER）_09654352.md`
