---
id: UNC@20.15.2@MMLCommand@LST EIR
type: MMLCommand
name: LST EIR（查询EIR配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EIR
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- EIR管理
status: active
---

# LST EIR（查询EIR配置）

## 功能

**适用网元：MME**

此命令用于查询EIR（Equipment Identity Register）表记录。MME（Mobility Management Entity）根据EIR表记录选择EIR。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EIR]] · EIR配置（EIR）

## 使用实例

查询系统内EIR表记录：

LST EIR:;

```
%%LST EIR:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
            EIR域名  =  example01.com
          EIR主机名  =  example01.com
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-EIR.md`
