---
id: UNC@20.15.2@MMLCommand@LST NGCBSFUNC
type: MMLCommand
name: LST NGCBSFUNC（查询小区广播功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGCBSFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 5G小区广播管理
status: active
---

# LST NGCBSFUNC（查询小区广播功能）

## 功能

**适用NF：AMF**

该命令用于查询小区广播功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGCBSFUNC]] · 小区广播功能（NGCBSFUNC）

## 使用实例

查询小区广播功能参数，执行如下命令：

```
%%LST NGCBSFUNC:;%%
RETCODE = 0  操作成功

结果如下
------------------------
               反馈功能开关  =  否
 小区广播任务老化时间(分钟)  =  20
小区广播消息发送速率(个/秒)  =  10000
     大区域分段并发预警开关  =  关闭
WarningAreaList信元精简开关  =  关闭
           预警结果上报策略  =  所有CBCF
           预警结果合并开关  =  关闭
     预警结果合并数量（个）  =  20
     预警结果缓存时长（秒）  =  2
      gNodeB ID有效比特长度  =  24
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGCBSFUNC.md`
