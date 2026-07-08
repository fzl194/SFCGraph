---
id: UNC@20.15.2@MMLCommand@LST SMSCCONVERT
type: MMLCommand
name: LST SMSCCONVERT（查询SMSC转换配置记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSCCONVERT
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 短消息
- SMSC转换
status: active
---

# LST SMSCCONVERT（查询SMSC转换配置记录）

## 功能

**适用网元：SGSN**

此命令用于查询SMSC转换记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REQADDR | 请求SMSC地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定请求SMSC地址。<br>“请求SMSC地址”<br>是手机短消息中携带的请求SMSC地址。<br>取值范围：1～16位十进制字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCCONVERT]] · SMSC转换配置记录（SMSCCONVERT）

## 使用实例

查询SMSC转换配置记录：

LST SMSCCONVERT:;

```
%%LST SMSCCONVERT:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
请求SMSC地址  =  8613951701
转换SMSC地址  =  8613951996
        描述  =  FOR MSC1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSCCONVERT.md`
