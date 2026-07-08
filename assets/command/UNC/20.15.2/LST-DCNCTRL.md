---
id: UNC@20.15.2@MMLCommand@LST DCNCTRL
type: MMLCommand
name: LST DCNCTRL（查询DCN控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DCNCTRL
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN控制参数
status: active
---

# LST DCNCTRL（查询DCN控制参数）

## 功能

**适用网元：MME**

此命令用于查询当前专用核心网重选处理方式。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DCNCTRL]] · DCN控制参数（DCNCTRL）

## 使用实例

查询当前配置的DCN控制参数：

LST DCNCTRL:;

```
%%LST DCNCTRL:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
                  重选策略  =  立即
         携带UE Usage Type  =  否
     UE USAGE TYPE携带策略  =  正在使用的UE USAGE TYPE
                 非广播TAI  =  0000000000
             MMEGI查询策略  =  使用本地配置查询MMEGI
              域名回退查询  =  NULL
     Backoff Timer分配开关  =  关闭
Back off timer最小值（秒）  =  300
Back off timer最大值（秒）  =  1800
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DCNCTRL.md`
