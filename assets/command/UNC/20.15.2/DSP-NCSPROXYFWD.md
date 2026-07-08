---
id: UNC@20.15.2@MMLCommand@DSP NCSPROXYFWD
type: MMLCommand
name: DSP NCSPROXYFWD（显示NETCONF代理转发策略）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCSPROXYFWD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# DSP NCSPROXYFWD（显示NETCONF代理转发策略）

## 功能

该命令用于显示NETCONF代理转发策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCSPROXYFWD]] · NETCONF代理转发策略（NCSPROXYFWD）

## 使用实例

显示NETCONF代理转发策略：

```
DSP NCSPROXYFWD:;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------

目标          VNFC标识    VNFC类型      模块              命名空间     

SirpAgent=0   1           VNFP          LogSirp           http://www.huawei.com/netconf/wireless-sirp/1.0                                                
SirpAgent=0   0           VNFP          netconf           http://www.huawei.com/netconf/vrp                               
SirpAgent=0   0           VNFP          AlarmSirp         http://www.huawei.com/netconf/wireless-sirp/1.0      
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCSPROXYFWD.md`
