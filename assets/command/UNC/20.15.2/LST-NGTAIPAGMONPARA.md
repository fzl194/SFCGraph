---
id: UNC@20.15.2@MMLCommand@LST NGTAIPAGMONPARA
type: MMLCommand
name: LST NGTAIPAGMONPARA（查询NG TAI组寻呼异常监控功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGTAIPAGMONPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 拥塞控制
- TA LIST流控
status: active
---

# LST NGTAIPAGMONPARA（查询NG TAI组寻呼异常监控功能参数）

## 功能

**适用NF：AMF**

该命令用于查询NG TAI寻呼异常监控检测参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NG TAI组寻呼异常监控功能参数（NGTAIPAGMONPARA）](configobject/UNC/20.15.2/NGTAIPAGMONPARA.md)

## 使用实例

查询NG TAI组寻呼异常监控检测参数信息。

```
%%LST NGTAIPAGMONPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                     TAI寻呼异常监控开关  =  关闭
        N2模式TAI组寻呼成功率初始值（%）  =  90
     N2模式TAI组寻呼请求次数起始监控阈值  =  1000
      N2模式TAI组寻呼成功率降幅阈值（%）  =  5
N2模式TAI组二次寻呼请求次数增幅阈值（%）  =  20
         TAI寻呼消息启控连续异常周期个数  =  1
                 语音业务TAI寻呼流控开关  =  关闭
                        寻呼最大重试次数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NG-TAI组寻呼异常监控功能参数（LST-NGTAIPAGMONPARA）_94289558.md`
