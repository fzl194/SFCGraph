---
id: UNC@20.15.2@MMLCommand@LST SMFMBSFUNC
type: MMLCommand
name: LST SMFMBSFUNC（查询MB-SMF组播广播功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFMBSFUNC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- MB-SMF组播广播功能管理
status: active
---

# LST SMFMBSFUNC（查询MB-SMF组播广播功能参数）

## 功能

**适用NF：SMF**

该命令用于查询MB-SMF组播广播功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFMBSFUNC]] · MB-SMF组播广播功能参数（SMFMBSFUNC）

## 使用实例

当需要查询MB-SMF 5G组播广播功能参数时，执行如下命令：

```
%%LST SMFMBSFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                   5G MBMS功能控制开关  =  不使能
                     TMGI失效时长(min)  =  1440
N11mb接口等待基站侧响应消息最大时长(s)  =  120
       N4mb接口等待响应消息最大时长(s)  =  180
                      N3mb接口传输方式  =  单播传输
           广播会话部分AMF故障处理方式  =  保留会话
        广播会话部分MB-UPF故障处理方式  =  保留会话
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MB-SMF组播广播功能参数（LST-SMFMBSFUNC）_82452582.md`
