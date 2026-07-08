---
id: UNC@20.15.2@MMLCommand@ADD PODISOBLKLIST
type: MMLCommand
name: ADD PODISOBLKLIST（增加Pod隔离黑名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PODISOBLKLIST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# ADD PODISOBLKLIST（增加Pod隔离黑名单）

## 功能

![](增加Pod隔离黑名单（ADD PODISOBLKLIST）_60519725.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该命令配置后对应类型的Pod出现Fabric平面通信亚健康或者通信故障场景将统一不进行隔离，可能会导致业务呼损，请谨慎使用并联系华为技术支持协助操作。

该命令用于增加指定Pod类型到Pod隔离黑名单中。

## 注意事项

- 该命令执行后立即生效。

- 该命令执行后不会影响业务正常运行，但当环境上对应的Pod类型出现Fabric平面通信亚健康或者通信故障时，则可能会导致业务呼损。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | Pod类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Pod隔离黑名单的Pod类型。可通过<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PODISOBLKLIST]] · Pod隔离黑名单（PODISOBLKLIST）

## 使用实例

将Pod类型“sbim-pod”增加到Pod隔离黑名单。

```
%%ADD PODISOBLKLIST: PODTYPE="sbim-pod";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PODISOBLKLIST.md`
