---
id: UNC@20.15.2@MMLCommand@DSP NGUSERNUM
type: MMLCommand
name: DSP NGUSERNUM（显示5G用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGUSERNUM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# DSP NGUSERNUM（显示5G用户数）

## 功能

**适用NF：AMF**

该命令用于查询AMF系统内各种用户状态的统计结果。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGUSERNUM]] · 5G用户数（NGUSERNUM）

## 使用实例

查看AMF上的用户数据统计结果，执行如下命令：

```
%%DSP NGUSERNUM:;%%
RETCODE = 0  操作成功

结果如下
------------------------
POD ID    静态用户数  动态用户数  PDU会话数  POD版本号信息

usn-pod-0 0           0           0          22.2.0.B060  
total     0           0           0          -            
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGUSERNUM.md`
