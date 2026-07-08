---
id: UDG@20.15.2@MMLCommand@SET HOSTDOMAINPARA
type: MMLCommand
name: SET HOSTDOMAINPARA（设置主机域参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HOSTDOMAINPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 主机域参数
status: active
---

# SET HOSTDOMAINPARA（设置主机域参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置主机域相关参数，通过该命令可以控制host是否全量学习。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 使能多Host学习开关, 对性能会产生一定影响，执行命令前请评估对性能的影响。
- 建议开启多Host学习开关后同步开启软参BIT361监控设备资源告警。
- 按需开启软参BIT2555以开启HOST全量学习功能后只对匹配中最高优先级的所有HOST进行学习的功能。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MULTIHOSTSTUDY |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MULTIHOSTSTUDY | 多Host学习开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否支持一个报文学习到多个Host。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HOSTDOMAINPARA]] · 主机域参数（HOSTDOMAINPARA）

## 使用实例

打开host全量学习开关：

```
%%SET HOSTDOMAINPARA: MULTIHOSTSTUDY=ENABLE;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-HOSTDOMAINPARA.md`
