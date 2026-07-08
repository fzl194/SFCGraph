---
id: UNC@20.15.2@MMLCommand@LST SCTPCCTRLPARA
type: MMLCommand
name: LST SCTPCCTRLPARA（查询RAN侧拥塞检测功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPCCTRLPARA
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# LST SCTPCCTRLPARA（查询RAN侧拥塞检测功能参数）

## 功能

**适用网元：MME、AMF**

该命令用于查询SCTP链路拥塞控制相关参数信息。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPCCTRLPARA]] · RAN侧拥塞检测功能参数（SCTPCCTRLPARA）

## 使用实例

查询RAN侧拥塞检测功能参数信息：

LST SCTPCCTRLPARA:;

```
%%LST SCTPCCTRLPARA:;%%
RETCODE = 0  操作成功
输出结果如下
------------------------
                  拥塞控制功能  =  关闭
                  拥塞控制算法  =  BBR拥塞控制算法
    低优先级消息流控时延（ms）  =  300
    高优先级消息流控时延（ms）  =  450
        发送缓存过载时延（ms）  =  800
            连续过载次数（个）  =  5
    发送缓存过载恢复时延（ms）  =  300
发送缓存连续正常状态时长（ms）  =  10000
     发送缓存过载比例门限（%）  =  80
 发送缓存过载恢复比例门限（%）  =  60
               告警上报周期数   =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RAN侧拥塞检测功能参数(LST-SCTPCCTRLPARA)_06728413.md`
