---
id: UNC@20.15.2@MMLCommand@LST NRFFCPKGMIX
type: MMLCommand
name: LST NRFFCPKGMIX（查询NRF大小包协同返回功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFFCPKGMIX
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF流控参数
status: active
---

# LST NRFFCPKGMIX（查询NRF大小包协同返回功能参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF大小包协同返回功能相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFFCPKGMIX]] · NRF大小包协同返回功能参数（NRFFCPKGMIX）

## 使用实例

当运营商希望查询NRF大小包协同返回功能相关参数时，执行此命令。

```
LST NRFFCPKGMIX:;
%%LST NRFFCPKGMIX:;%%
RETCODE = 0  操作成功
结果如下
-------------------------
    大小包协同返回功能开关  =  打开
     大包比例递减周期 (秒)  =  3
大包比例递减的公比的百分比  =  90
     大包比例抑制时长 (秒)  =  360
   恢复大包比例的周期 (秒)  =  6
  大包比例恢复的公差百分比  =  3
       带宽速率上限 (MB/s)  =  25
     解除带宽控制周期 (秒)  =  120
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFFCPKGMIX.md`
