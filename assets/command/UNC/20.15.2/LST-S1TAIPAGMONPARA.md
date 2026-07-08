---
id: UNC@20.15.2@MMLCommand@LST S1TAIPAGMONPARA
type: MMLCommand
name: LST S1TAIPAGMONPARA（查询S1 TAI组寻呼异常监控功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1TAIPAGMONPARA
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- S1寻呼流控管理
- TA LIST流控
status: active
---

# LST S1TAIPAGMONPARA（查询S1 TAI组寻呼异常监控功能参数）

## 功能

**适用网元：MME**

该命令用于查询S1 TAI组对象寻呼异常监控功能的参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1TAIPAGMONPARA]] · S1 TAI组寻呼异常监控功能参数（S1TAIPAGMONPARA）

## 使用实例

查询S1 TAI组寻呼异常监控配置。

LST S1TAIPAGMONPARA:;

```
%%LST S1TAIPAGMONPARA:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                      TAI寻呼异常监控开关 =  关闭
        S1模式TAI组寻呼成功率初始值（%）  =  90
     S1模式TAI组寻呼请求次数起始监控阈值  =  1000
      S1模式TAI组寻呼成功率降幅阈值（%）  =  5
S1模式TAI组二次寻呼请求次数增幅阈值（%）  =  50
         TAI寻呼消息启控连续异常周期个数  =  1
                        寻呼最大重试次数  =  0
                 语音业务TAI寻呼流控开关  =  关闭
                                告警开关  =  开启
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1-TAI组寻呼异常监控功能参数(LST-S1TAIPAGMONPARA)_27678301.md`
