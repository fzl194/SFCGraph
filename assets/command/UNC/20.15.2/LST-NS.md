---
id: UNC@20.15.2@MMLCommand@LST NS
type: MMLCommand
name: LST NS（查询NS参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NS
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- NS参数
status: active
---

# LST NS（查询NS参数）

## 功能

**适用网元：SGSN**

该命令用于查询NS层系统参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NS]] · NS参数（NS）

## 使用实例

查询NS参数：

LST NS:;

```
%%LST NS:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                   Block定时器(s)   =  120
                    Block重试次数   =  3
                  Unblock重试次数   =  3
                    复位定时器(s)   =  10
                     复位重试次数   =  3
                    测试定时器(s)   =  30
                   Alive定时器(s)   =  3
                     Alive重试次数  =  10
                       Prov定时器   =  5
                     Prov重试次数   =  3
    自动配置的NSE的上报速率(个/秒)  =  5
自动配置的NSE的故障删除时长（分钟） =  0
            自动配置的NSE的分布策略 =  整系统分布

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NS.md`
