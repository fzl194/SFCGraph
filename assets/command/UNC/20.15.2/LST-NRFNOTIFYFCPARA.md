---
id: UNC@20.15.2@MMLCommand@LST NRFNOTIFYFCPARA
type: MMLCommand
name: LST NRFNOTIFYFCPARA（查询通知流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNOTIFYFCPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF流控参数
status: active
---

# LST NRFNOTIFYFCPARA（查询通知流控参数）

## 功能

**适用NF：NRF**

该命令用于查询通知流程的固定速率流控信息 。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [通知流控参数（NRFNOTIFYFCPARA）](configobject/UNC/20.15.2/NRFNOTIFYFCPARA.md)

## 使用实例

查询通知流程的固定速率流控信息：

```
%%LST NRFNOTIFYFCPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
        NFPROFILE变更事件流控开关  =  关闭
  每秒处理NFPROFILE变更事件的数量  =  0
             失败通知重传流控开关  =  打开
       每秒处理失败通知重传的数量  =  100
       NF更新事件缓冲最长时长(秒)  =  720
       NF更新事件最短缓冲时长(秒)  =  300
           NF更新事件合并日志个数  =  50
           NF订阅通知队列最大长度  =  3000
     单个VM发送订阅通知带宽(MB/S)  =  6
     单个VM发送订阅通知个数(个/S)  =  500
       NF心跳类型变更增量通知开关  =  打开
   NF状态变更事件最短缓冲时长(秒)  =  30
   NF状态变更事件最长缓冲时长(秒)  =  600
 NF状态变更增量通知携带NFTYPE开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询通知流控参数（LST-NRFNOTIFYFCPARA）_09654449.md`
