---
id: UNC@20.15.2@MMLCommand@LST NRFINTERFUNC
type: MMLCommand
name: LST NRFINTERFUNC（查询国际漫游功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFINTERFUNC
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# LST NRFINTERFUNC（查询国际漫游功能参数）

## 功能

**适用NF：NRF**

此命令用于查询NRF国际漫游功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [国际漫游功能参数（NRFINTERFUNC）](configobject/UNC/20.15.2/NRFINTERFUNC.md)

## 使用实例

使用以下命令查询国际漫游功能参数。

```
%%LST NRFINTERFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
        服务发现V-SMF精确匹配开关  =  关闭
    跨PLMN订阅更新是否返回404开关  =  打开
                   故障重选状态码  =  429.500.502.503.504
          HPLMN NRF的标准FQDN开关  =  关闭
              HPLMN NRF的协议模式  =  HTTP
     本NRF是否是国际漫游关口局NRF  =  是
漫游服务发现InterPlmnFqdn过滤开关  =  关闭
                 ProxySMF功能开关  =  关闭
         ProxySMF不匹配时处理策略  =  转发至对端I-NRF
    发现ProxySMF的DNN网络标识列表  =  ims
       漫入SUPI服务发现白名单开关  =  关闭
      允许ProxySMF网内发现开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询国际漫游功能参数（LST-NRFINTERFUNC）_24956636.md`
