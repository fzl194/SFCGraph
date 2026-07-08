---
id: UNC@20.15.2@MMLCommand@LST NRFLOGSW
type: MMLCommand
name: LST NRFLOGSW（查询NRF维护日志打印开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFLOGSW
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF维测管理
status: active
---

# LST NRFLOGSW（查询NRF维护日志打印开关）

## 功能

**适用NF：NRF**

该命令用于查询NRF的维护日志打印开关的值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFLOGSW]] · NRF维护日志打印开关（NRFLOGSW）

## 使用实例

当维护人员希望查看当前NRF维护日志打印开关的值时，执行如下命令：

```
%%LST NRFLOGSW:;%%
RETCODE = 0  操作成功

结果如下
--------
       服务发现日志打印开关  =  打开
         NF检索日志打印开关  =  关闭
   NF注册和更新日志打印开关  =  打开
         NF订阅日志打印开关  =  关闭
           通知日志打印开关  =  关闭
服务发现日志打印速率(次/秒)  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFLOGSW.md`
