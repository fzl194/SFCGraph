---
id: UNC@20.15.2@MMLCommand@DSP DNSS
type: MMLCommand
name: DSP DNSS（显示DNS服务器状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DNSS
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS服务器管理
status: active
---

# DSP DNSS（显示DNS服务器状态）

## 功能

**适用网元：SGSN、MME** **、AMF**

该命令用于查看DNS服务器的状态。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNSS]] · DNS服务器（DNSS）

## 使用实例

查询DNS服务器信息：

DSP DNSS:;

```
%%DSP DNSS:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
 服务器组ID    IP地址类型     IP地址           域名服务器优先级   DNS服务器名称     服务器状态   是否支持递归
 0            IPV4           192.168.179.1   优先级1           NULL              正常        不支持
 1            IPV4           192.168.179.2   优先级1           NULL              故障        不支持
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DNSS.md`
