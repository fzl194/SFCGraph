---
id: UNC@20.15.2@MMLCommand@MOD TLSPARA
type: MMLCommand
name: MOD TLSPARA（修改TLS参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: TLSPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS安全管理
status: active
---

# MOD TLSPARA（修改TLS参数）

## 功能

该命令用于修改一组TLS参数。

## 注意事项

- 该命令执行后立即生效。

- 如果修改TLSPARA中除“描述”外的参数，需要先执行[**ADD TLSPARA**](增加TLS参数（ADD TLSPARA）_84132096.md)命令增加一条记录，然后执行[**MOD HTTPLE**](../../HTTP本端实体管理/修改HTTP本端实体（MOD HTTPLE）_28971845.md)MOD HTTPLE命令，将“TLS索引”参数修改为[**ADD TLSPARA**](增加TLS参数（ADD TLSPARA）_84132096.md)命令新增加的索引值。操作后对新建立的HTTPS链路生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TLS参数索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>与<br>[**ADD HTTPLE**](../../HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)<br>中配置的TLS参数索引保持一致。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TLS上下文描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TLSPARA]] · TLS参数（TLSPARA）

## 使用实例

若运营商想修改索引为1的TLS配置的描述，可以用如下命令：

```
MOD TLSPARA:  INDEX=1, DESC= "mod tlspara";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-TLSPARA.md`
