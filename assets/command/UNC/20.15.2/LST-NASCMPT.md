---
id: UNC@20.15.2@MMLCommand@LST NASCMPT
type: MMLCommand
name: LST NASCMPT（查询NAS兼容性参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NASCMPT
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- NAS兼容性参数管理
status: active
---

# LST NASCMPT（查询NAS兼容性参数）

## 功能

**适用NF：AMF**

该命令用于查询NAS（Non-Access-Stratum protocol）兼容性控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NASMSGTYPE | NAS消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NAS消息类型，根据消息类型来确认是否需要配置相应的消息接口兼容性。<br>数据来源：全网规划<br>取值范围：<br>- “REGISTRATION_REJECT（注册拒绝消息）”：AMF发给UE的注册拒绝消息。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NASCMPT]] · NAS兼容性参数（NASCMPT）

## 使用实例

查询系统中当前配置的NAS兼容性参数，执行如下命令：

```
LST NASCMPT:;
%%LST NASCMPT:;%%
RETCODE = 0  操作成功
结果如下
--------
         NAS消息类型 = 注册拒绝消息
是否携带拒绝切片信元 = 否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NASCMPT.md`
