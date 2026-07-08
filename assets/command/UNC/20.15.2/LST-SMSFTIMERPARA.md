---
id: UNC@20.15.2@MMLCommand@LST SMSFTIMERPARA
type: MMLCommand
name: LST SMSFTIMERPARA（查询SMSF网元定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFTIMERPARA
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 定时器管理
status: active
---

# LST SMSFTIMERPARA（查询SMSF网元定时器）

## 功能

**适用NF：SMSF**

该命令用于查看SMSF配置的相关业务定时器信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFTIMERPARA]] · SMSF网元定时器（SMSFTIMERPARA）

## 使用实例

查询SMSF相关业务定时器信息，执行如下命令：

```
%%LST SMSFTIMERPARA:;%%
RETCODE = 0  操作成功
结果如下
------------------------
               TOPO查询定时器(秒)  =  6
               UDM 注册定时器(秒)  =  6
             UDM 去注册定时器(秒)  =  6
     获取注册或签约数据定时器(秒)  =  6
                   订阅定时器(秒)  =  6
           N1N2消息传输定时器(秒)  =  4
   等待map open confirm定时器(秒)  =  6
等待map service confirm定时器(秒)  =  6
             等待UE消息定时器(秒)  =  4
               UE可达性定时器(秒)  =  14
         等待注册中心激活响应定时器(秒) = 6
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSFTIMERPARA.md`
