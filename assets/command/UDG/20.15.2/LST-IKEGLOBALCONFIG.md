---
id: UDG@20.15.2@MMLCommand@LST IKEGLOBALCONFIG
type: MMLCommand
name: LST IKEGLOBALCONFIG（查询IKE全局配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IKEGLOBALCONFIG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE全局配置
status: active
---

# LST IKEGLOBALCONFIG（查询IKE全局配置）

## 功能

该命令用于查询IKE全局配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IKEGLOBALCONFIG]] · IKE全局配置（IKEGLOBALCONFIG）

## 使用实例

查询IKE全局配置：

```
LST IKEGLOBALCONFIG:;
    RETCODE = 0  操作成功

结果如下
-------------------------
          清除分片标记位  =  FALSE
              加密前分片  =  FALSE
流量方式触发SA过期标记位 = FALSE
         流量数（kbyte）  =  1843200
           时间间隔（s）  =  3600
                  抗重放  =  TRUE
                窗口大小  =  Global window size 1024
                本地名称  =  NULL
        DPD检查间隔（s）  =  NULL
                 DPD类型  =  无
        DPD重试间隔（s）  =  99
        历史信息记录条数  =  30    
            安全日志阈值  =  0 
     NAT保活时间间隔 (s)  =  20 
IPSEC转发CPU过载告警上报阈值 (%) = 80
IPSEC转发CPU过载告警恢复阈值 (%) = 70
         UIKE主动核查时间 =  4
IPsec跟踪的开启流控的CPU阈值（%） = 80
IPsec跟踪的恢复流控的CPU阈值（%） = 65
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IKEGLOBALCONFIG.md`
