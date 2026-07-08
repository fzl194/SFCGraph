---
id: UNC@20.15.2@MMLCommand@LST S1UBLACKLSTPARA
type: MMLCommand
name: LST S1UBLACKLSTPARA（查询S1-U黑名单参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1UBLACKLSTPARA
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1-U黑名单管理
- S1-U黑名单规则
status: active
---

# LST S1UBLACKLSTPARA（查询S1-U黑名单参数）

## 功能

**适用网元：MME**

暂不支持本命令。此命令用于查询S1-U IP地址黑名单参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1UBLACKLSTPARA]] · S1-U黑名单参数（S1UBLACKLSTPARA）

## 使用实例

查询S1-U黑名单参数：

LST S1UBLACKLSTPARA:;

```
%%LST S1UBLACKLSTPARA:;%% 
RETCODE = 0  操作成功  

输出结果如下： 
-------------- 
发送黑名单策略  =  发送 
(结果个数 = 1)

---    END
```

**输出结果说明**

参见 **[SET S1UBLACKLSTPARA](设置S1-U黑名单参数(SET S1UBLACKLSTPARA)_89145434.md)** 的参数说明。

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-S1UBLACKLSTPARA.md`
