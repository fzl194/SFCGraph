---
id: UNC@20.15.2@MMLCommand@LST NSACTRL
type: MMLCommand
name: LST NSACTRL（查询NSA控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSACTRL
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- NSA组网管理
- NSA控制参数
status: active
---

# LST NSACTRL（查询NSA控制参数）

## 功能

**适用网元：MME**

该命令用于查询NSA组网场景下的整系统控制参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug。
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组。

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSACTRL]] · NSA控制参数（NSACTRL）

## 使用实例

查询NSA控制参数：

LST NSACTRL:;

```
%%LST NSACTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                       NR流量上报  =  否
DNS查询对等网元时是否携带NCNR标志  =  否
                         流量区分  =  否
    MME通知HSS是否为NSA用户的方式  =  功能关闭
            PSCell ID消息清除选项  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSACTRL.md`
