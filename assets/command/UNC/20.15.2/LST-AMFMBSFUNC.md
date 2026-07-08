---
id: UNC@20.15.2@MMLCommand@LST AMFMBSFUNC
type: MMLCommand
name: LST AMFMBSFUNC（查询AMF组播广播功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFMBSFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- AMF组播广播管理
- AMF组播广播功能管理
status: active
---

# LST AMFMBSFUNC（查询AMF组播广播功能参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF组播广播功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [AMF组播广播功能参数（AMFMBSFUNC）](configobject/UNC/20.15.2/AMFMBSFUNC.md)

## 使用实例

查询AMF组播广播功能参数，执行如下命令：

```
%%LST AMFMBSFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                广播功能开关  =  关闭
            广播切片使能开关  =  否
    广播流程最大响应时间(秒)  =  600
      是否支持不携带广播区域  =  否
      N2接口携带广播区域策略  =  尽力携带全量广播区域
            广播流程响应模式  =  协议模式
        是否支持广播区域更新  =  是
     广播消息发送速率(个/秒)  =  3000
N11mb接口携带基站TAI列表开关  =  否
    广播会话超期协商功能开关  =  否
    广播会话超期时间协商策略  =  优先使用MB-SMF携带的超期时间
      广播会话超期间隔(分钟)  =  60
    广播会话超期宽限期(分钟)  =  15
    基站配置更新场景增强开关  =  是
        基站故障场景增强开关  =  是
                广播重试开关  =  否
          重试间隔时间(分钟)  =  120
    广播通知响应异常处理开关  =  是
        单广播会话支持基站数  =  50000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF组播广播功能参数（LST-AMFMBSFUNC）_86212798.md`
