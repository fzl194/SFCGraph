---
id: UNC@20.15.2@MMLCommand@DSP VLR
type: MMLCommand
name: DSP VLR（显示VLR迁移进度）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VLR
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- VLR管理
status: active
---

# DSP VLR（显示VLR迁移进度）

## 功能

**适用网元：SGSN、MME**

该命令用于查询VLR迁移进度信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VLR在移动网络中的设备号。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值： 无。 |
| POOLNM | MSC POOL名称 | 可选必选说明：可选参数<br>参数说明：该参数用于指定MSC POOL名称。<br>数据来源：整网规划<br>取值范围：最大长度为19的字符串<br>默认值：无。<br>说明：- POOLNM唯一标识一个MSC POOL。当此参数没有输入任何值的时候表示新增加的VLR不属于任何MSC POOL。此参数大小写敏感，不支持含有中文字符，不支持包含非法字符，如逗号、分号、冒号、等号、加号、减号、单引号、双引号、百分号。<br>- POOLNM的值不能设置为NULL（这里字符N，U和L不区分大小写）。 |
| OFFLOADSTA | 迁移状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VLR目前的迁移状态。<br>数据来源：整网规划<br>取值范围：<br>- “NORMAL（正常）”<br>- “OFFLOAD_MANUALLY（手动迁移中）”<br>- “OFFLOAD_AUTO（自动迁移中）”<br>默认值： 无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLR]] · VLR配置信息（VLR）

## 使用实例

1. 查询VLR迁移进度信息：
  **DSP VLR:;**
  ```
  %%DSP VLR: VN="1230301";%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------

         VLR号 = 1230301
       VLR名称 = VLR1
  MSC POOL名称 = NULL
       最小V值 = 0
       最大V值 = 999
   附加最小V值 = NULL
   附加最大V值 = NULL
      迁移状态 = 正常
      迁移阶段 = 初始化
        用户数 = 0
  剩余迁移时间 = 0
  （结果个数 = 1）

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示VLR迁移进度(DSP-VLR)_26305256.md`
