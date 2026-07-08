---
id: UNC@20.15.2@MMLCommand@LST LOCALHSS
type: MMLCommand
name: LST LOCALHSS（查询本地HSS）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALHSS
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- LOCALHSS管理
status: active
---

# LST LOCALHSS（查询本地HSS）

## 功能

**适用网元：MME**

该命令用于查询本地HSS信息。

## 注意事项

- 此命令执行后立即生效。
- 此命令不区分主机名中的大小写字母，系统统一按照大写字母来处理。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSSHTNAM | 本地HSS主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地HSS主机名。<br>数据来源：整网规划<br>取值范围：0~127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如:hss.epc.mnc123.mcc123.3gppnetwork.org<br>- 不允许配置字符串“NULL”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALHSS]] · 本地HSS（LOCALHSS）

## 使用实例

- 该命令用于查询本地HSS信息：
  LST LOCALHSS:;
  ```
  %%LST LOCALHSS:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  -------------------------
   本地HSS主机名            本地HSS名称

   HSS1502.HUAWEI03.COM.CN  localhss1
   HSS150.HUAWEI03.COM.CN   localhss2
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地HSS(LST-LOCALHSS)_72225759.md`
