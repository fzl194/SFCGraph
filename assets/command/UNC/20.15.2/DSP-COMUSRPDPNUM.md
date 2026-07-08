---
id: UNC@20.15.2@MMLCommand@DSP COMUSRPDPNUM
type: MMLCommand
name: DSP COMUSRPDPNUM（显示移动性管理用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMUSRPDPNUM
command_category: 查询类
applicable_nf:
- MME
- SGSN
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 融合接入业务管理
- 融合用户数据库管理
status: active
---

# DSP COMUSRPDPNUM（显示移动性管理用户数）

## 功能

**适用NF：MME、SGSN、AMF**

该命令用于查询系统内各种用户状态的统计结果。

## 注意事项

5G用户、234G用户和NB-IoT用户状态的统计结果也可以通过DSP NGUSERNUM和DSP USRPDPNUM命令来查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMUSRPDPNUM]] · 移动性管理用户数（COMUSRPDPNUM）

## 使用实例

查询系统内各种用户状态的统计结果，执行如下命令：

```
%%DSP COMUSRPDPNUM:;%%
RETCODE = 0  操作成功

结果如下
--------
       234G静态用户数  =  0
         5G静态用户数  =  0
      APN签约上下文数  =  0
         2G在线用户数  =  0
         3G在线用户数  =  0
         4G在线用户数  =  0
         5G在线用户数  =  0
     NB-IoT在线用户数  =  0
        2G激活PDP个数  =  0
        3G激活PDP个数  =  0
         4G EPS承载数  =  0
          5GPDU会话数  =  0
         NB-IoT承载数  =  0
     NB-IoT服务用户数  =  0
             NR承载数  =  0
         NR在线用户数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-COMUSRPDPNUM.md`
