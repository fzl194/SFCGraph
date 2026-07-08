---
id: UNC@20.15.2@MMLCommand@SYN CMFDATA
type: MMLCommand
name: SYN CMFDATA（强制推送集群管理数据）
nf: UNC
version: 20.15.2
verb: SYN
object_keyword: CMFDATA
command_category: 动作类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SYN CMFDATA（强制推送集群管理数据）

## 功能

![](强制推送集群管理数据（SYN CMFDATA）_99312746.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，执行后可能引起性能下降，且频繁操作会导致CPU升高，请谨慎使用并联系华为技术支持协助操作。

该命令用于集群管理服务向客户端强制同步集群管理数据。

## 注意事项

- 等待180s集群管理数据同步完成后生效

- 该命令用于数据不一致导致紧急问题时强制推送全量集群管理数据，非紧急情况下请勿执行。
- 为避免频繁执行对系统性能产生冲击，该命令在三分钟之内只能执行一次。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SYNCMODE | 推送模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定以何种方式进行强制数据同步。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（所有）”：CMF向所有客户端强制推送集群管理数据。<br>- “BYPODID（Pod ID）”：CMF向指定的Pod强制推送集群管理数据。<br>默认值：无<br>配置原则：无 |
| PODID | Pod ID | 可选必选说明：该参数在"SYNCMODE"配置为"BYPODID"时为条件必选参数。<br>参数含义：该参数用于指定Pod进行强制数据同步。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：<br>Pod ID可以通过<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>命令查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CMFDATA]] · 强制推送集群管理数据（CMFDATA）

## 使用实例

指定Pod同步集群管理数据，PodID为vup-pod-0。

```
%%%%SYN CMFDATA: SYNCMODE=BYPODID, PODID="vup-pod-0";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SYN-CMFDATA.md`
